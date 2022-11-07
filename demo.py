
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation
def main():
    try:
          pipeline = Pipeline()
          pipeline.run_pipeline()
          #data_validation_config=Configuartion().get_data_transformation_config()
          #print(data_validation_config)
          #schema_file_path = r"C:\project\machine_learning_project\config\schema.yaml"
          
          
    except Exception as e:
        logging.error(f"{e}")
        print(e)
    

if __name__ == "__main__":
    main()
