"""Check saved evidence identity and consistency. Does not train models or access Kaggle."""
from pathlib import Path
import ast, csv, hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
rows=list(csv.DictReader((ROOT/'results/submission_history.csv').open()))
assert len(rows)==14 and len({r['submission_filename'] for r in rows})==14
assert max(float(r['confirmed_public_score']) for r in rows)==.9806
best=ROOT/'results/best_ensemble/submission_best75_convnextv2_tta25.csv'
assert digest(best)=='8d255cfb971b031801ac95e8600fdada6eb0d51190b993e472b305d148639d23'
ids=list(csv.DictReader(best.open()))
assert len(ids)==29443 and len({r['image_id'] for r in ids})==29443
for entry in json.loads((ROOT/'docs/notebook_provenance.json').read_text()):
    assert digest(ROOT/entry['path'])==entry['sha256'],entry['path']
for entry in json.loads((ROOT/'results/evidence/index.json').read_text()):
    assert digest(ROOT/entry['path'])==entry['sha256'],entry['path']
for number in ['07','08','09','10']:
    paths=list((ROOT/'notebooks').glob(number+'-*.ipynb'));assert len(paths)==1
    nb=json.loads(paths[0].read_text());code=[c for c in nb['cells'] if c['cell_type']=='code']
    for cell in code:
        ast.parse(''.join(cell['source']))
        assert not any(o.get('output_type')=='error' for o in cell.get('outputs',[]))
    if number=='10':
        assert [c.get('execution_count') for c in code]==list(range(1,8))
        prepared=json.loads((ROOT/'archive/10-dinov2-base224-prepared.ipynb').read_text())
        pcode=[c for c in prepared['cells'] if c['cell_type']=='code']
        assert all(ast.dump(ast.parse(''.join(a['source'])))==ast.dump(ast.parse(''.join(b['source']))) for a,b in zip(code,pcode))
        assert len(pcode)==len(code)==7
status=json.loads((ROOT/'results/dinov2_base224/status.json').read_text())
assert status['status']=='completed_submitted' and status['public_score']==.9806
assert status['selected_epoch']==8 and status['completed_epochs']==8 and status['kaggle_execution_evidence_received']
for key,record in json.loads((ROOT/'results/public_followups.json').read_text()).items():
    assert record['submitted'] is True and (ROOT/record['public_score_evidence']).is_file()
    match=[r for r in rows if r['submission_filename']==record['filename']];assert len(match)==1
    assert float(match[0]['confirmed_public_score'])==record['new_public_score']
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix in ['.ipynb','.py','.md','.json','.txt']:
        assert not re.search(r'(?:hf_[A-Za-z0-9]{24,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})',path.read_text()),path


# The tied submission is independently fingerprinted and aligned with the earlier selected CSV.
dino=ROOT/'results/dinov2_base224'
result=json.loads((dino/'public_result.json').read_text())
candidate=dino/result['filename']
assert result['submitted'] and result['new_public_score']==.9806
assert digest(candidate)==result['candidate_sha256']=='03c736b816cc3e87733602c2c374aeaf2b0c2be4fdcc00f06e8bf1d359c85fef'
alternative=list(csv.DictReader(candidate.open()))
assert [r['image_id'] for r in alternative]==[r['image_id'] for r in ids]
classes=json.loads((ROOT/'results/best_ensemble/classes.json').read_text())
assert all(r['class'] in classes for r in alternative)
assert sum(a['class']!=b['class'] for a,b in zip(alternative,ids))==134
history=list(csv.DictReader((dino/'history.csv').open()))
assert [int(r['epoch']) for r in history]==list(range(1,9))
complete=json.loads((dino/'training_complete.json').read_text())
assert digest(dino/'history.csv')==complete['history_sha256']
assert complete['best_epoch']==8 and int(history[-1]['val_errors'])==24
table=list(csv.DictReader((dino/'original_validation_comparison.csv').open()))
primary=[r for r in table if r['view']=='tta' and r['candidate']=='fixed_25pct_blend' and r['group']=='all_validation']
assert len(primary)==1 and tuple(int(primary[0][k]) for k in ['images','errors','fixed','broken'])==(9547,18,5,0)
for name,expected in [('dinov2_clean',24),('dinov2_tta',29),('blend25_clean',18),('blend25_tta',18)]:
    matrix=list(csv.reader((dino/('confusion_matrix_'+name+'.csv')).open()))
    values=[[int(x) for x in r[1:]] for r in matrix[1:]]
    assert matrix[0][1:]==classes and [r[0] for r in matrix[1:]]==classes
    assert sum(sum(r) for r in values)==9547
    assert 9547-sum(values[i][i] for i in range(8))==expected
assert result['evidence_sha256']==digest(ROOT/result['public_score_evidence'])
print('Verified executed notebooks and preserved prepared source, 14 confirmed public outcomes, both 0.9806 CSVs, score evidence and DINOv2 histories/comparisons/confusion matrices.')
