# ethio_medical_dw

A data warehouse project for Ethiopian medical data, featuring data collection, cleaning, object detection, and loading into PostgreSQL.

## Project Structure

- `config.py` – Project configuration settings.
- `requirements.txt` – Python dependencies.
- `yolov5s.pt` – Pretrained YOLOv5 model weights.
- `data/` – Raw, processed, and image data.
- `ethio_med_dwh/` – dbt project for data warehousing.
- `logs/` – Log files.
- `scripts/` – Data processing and ETL scripts.
- `yolov5/` – YOLOv5 source code and models.

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd ethio_medical_dw
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure the project**
   - Edit `config.py` with your settings.

## Usage

- **Data Cleaning:**  
  Run data cleaning scripts in `scripts/data_cleaner.py`.

- **Object Detection:**  
  Use `scripts/object_detection.py` with YOLOv5 models in `yolov5/`.

- **Load to PostgreSQL:**  
  Use `scripts/load_to_postgress.py` to load processed data into your database.

- **Telegram Scraper:**  
  Collect data from Telegram using `scripts/telegram_scrapper.py`.

- **Data Warehouse:**  
  Use dbt in `ethio_med_dwh/` for data modeling and analytics.  
  - Run `dbt run` to execute models and transform your data.
  - Run `dbt test` to validate your data and ensure data quality.
  - Run `dbt docs generate` to build project documentation.
  - Run `dbt docs serve` to view interactive documentation in your browser.

## YOLOv5

The `yolov5/` directory contains the official YOLOv5 codebase for object detection and classification.  
See [yolov5/README.md](yolov5/README.md) for details.

## License

See [yolov5/LICENSE](yolov5/LICENSE) for licensing information.

## Contact

For questions, open an issue or contact the maintainers.
