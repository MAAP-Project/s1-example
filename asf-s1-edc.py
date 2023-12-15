import boto3
import os
import argparse
import random

from maap.maap import MAAP
maap = MAAP()

def get_s3_creds(url:str):
    return maap.aws.earthdata_s3_credentials(url)

def get_s3_client(s3_cred_endpoint:str):
    # create the boto3 session
    creds=get_s3_creds(s3_cred_endpoint)
    boto3_session = boto3.Session(
            aws_access_key_id=creds['accessKeyId'],
            aws_secret_access_key=creds['secretAccessKey'],
            aws_session_token=creds['sessionToken']
    )
    return boto3_session.client("s3")

def download_s3_file(s3, bucket:str, file_name:str, dest:str) -> str:
    os.makedirs(dest, exist_ok=True) # create directories, as necessary
    download_path=f"{dest}/{os.path.basename(file_name)}"
    s3.download_file(bucket, f"{file_name}", download_path)
    return download_path


def download_test(output:str):
    results = maap.searchGranule(cmr_host="cmr.earthdata.nasa.gov",
        short_name='SENTINEL-1A_SLC',
        bounding_box='-124.8136026553671,32.445063449213436,-113.75989347462286,42.24498423828791',
        limit=20,
        temporal='2023-06-01T00:00:00Z,2030-06-12T23:59:59Z'
        )

    # pick a random granule
    select = random.randrange(0,19,1)
    sample = results[select].getDownloadUrl()

    # split into bucket and prefix
    split_path = os.path.split(sample)
    bucket = split_path[0].replace('s3://','')
    prefix = '/'.join(split_path[1:])
    
    # Get temporary S3 credentials
    asf_s3 = "https://sentinel1.asf.alaska.edu/s3credentials"
    #s3 = get_s3_creds(asf_s3)
    s3 = get_s3_client(asf_s3)
    
    #download
    print(f"Downloading {prefix}")
    download_path = download_s3_file(s3, bucket, prefix, output)
    
    
if __name__ == "__main__":
    # If we add args then parse them here
    parser = argparse.ArgumentParser(description='Download a S1 scene')
    parser.add_argument('--dest', dest="dest", type=str,
                    help='A string to the output directory destination')
    
    args = parser.parse_args()
    
    output = args.dest
    download_test(output)