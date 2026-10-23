"""Check saved evidence identity and consistency. Does not train models or access Kaggle."""
from pathlib import Path
import ast, csv, hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
rows=list(csv.DictReader((ROOT/'results/submission_history.csv').open()))
assert len(rows)==13 and len({r['submission_filename'] for r in rows})==13
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
    if number=='10': assert all(c.get('execution_count') is None and not c.get('outputs') for c in code)
status=json.loads((ROOT/'results/dinov2_base224/status.json').read_text())
assert status['status']=='running_user_reported' and status['public_score'] is None
assert status['validation_metrics'] is None and not status['kaggle_execution_evidence_received']
for key,record in json.loads((ROOT/'results/public_followups.json').read_text()).items():
    assert record['submitted'] is True and (ROOT/record['public_score_evidence']).is_file()
    match=[r for r in rows if r['submission_filename']==record['filename']];assert len(match)==1
    assert float(match[0]['confirmed_public_score'])==record['new_public_score']
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix in ['.ipynb','.py','.md','.json','.txt']:
        assert not re.search(r'(?:hf_[A-Za-z0-9]{24,}|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})',path.read_text()),path
print('Verified saved notebooks, score evidence, 13 confirmed outcomes, unchanged winning CSV and unscored Notebook 10 status.')
