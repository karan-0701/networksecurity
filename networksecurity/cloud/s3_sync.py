import subprocess

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = ["aws", "s3", "sync", folder, aws_bucket_url]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Failed to sync to S3: {result.stderr}")
        else:
            print(result.stdout)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = ["aws", "s3", "sync", aws_bucket_url, folder]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Failed to sync from S3: {result.stderr}")
        else:
            print(result.stdout)
