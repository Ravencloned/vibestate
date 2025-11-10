param(
    [string]$dataset = "example"
)

Write-Host "Placeholder downloader. Edit this file to download your dataset."
Write-Host "Examples:"
Write-Host " - Kaggle CLI: kaggle datasets download -d owner/dataset -p data/raw --unzip"
Write-Host " - Direct URL: Invoke-WebRequest -Uri 'https://example.com/data.zip' -OutFile 'data/raw/data.zip'; Expand-Archive -Path data/raw/data.zip -DestinationPath data/raw"
