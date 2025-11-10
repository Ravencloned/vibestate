Write-Host "1) Run make_dataset"
python -c "from src.data import make_dataset; import sys; sys.exit(0)"

Write-Host "2) Preprocess"
python src/data/preprocess.py

Write-Host "3) Build features"
python src/features/build_features.py

Write-Host "4) Train"
python src/models/train.py

Write-Host "5) Evaluate"
python src/models/evaluate.py
