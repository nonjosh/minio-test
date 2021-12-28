"""
./bin/mc -C .mc mb myminio/test
./bin/mc -C .mc cp --recursive data/test/ myminio/test/
"""
# %%
import json
import s3fs
import pandas as pd

# %%
fs = s3fs.S3FileSystem(
    anon=False,
    key="minio",
    secret="minio123",
    client_kwargs={
        "endpoint_url": "http://localhost:9000",
    },
)
# %%
# List files/folders in bucket
fs.ls("test")
# %%
# Read csv files
with fs.open("test/people.csv", "rb") as f:
    my_df = pd.read_csv(f)
my_df
# %%
# DataFrame add one row
my_df.loc[len(my_df)] = ["John", "18"]
my_df
# %%
# Write back to MinIO
with fs.open("test/people2.csv", "w") as f:
    my_df.to_csv(f)
with fs.open("test/people2.csv", "rb") as f:
    my_df = pd.read_csv(f)
my_df
# %%
# Read parquet files (require pyarrow)
with fs.open("test/people.parquet", "rb") as f:
    my_df = pd.read_parquet(f)
my_df
# %%
# Read compressed csv files
with fs.open(
    "mycsvbucket/sampledata/TotalPopulation.csv.gz", "rb", compression="gzip"
) as f:
    my_df = pd.read_csv(f)
my_df
# %%
# Read json files
with fs.open("test/people.json", "r") as f:
    my_json = json.load(f)
my_json
# %%
