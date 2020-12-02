from secret import aws_key_id, aws_secret_key
import boto3

from data_fetch import Data_Fetch

class Fire_Hose:

    def __init__(self):
        firehose_client = boto3.client('firehose', 
                                region_name = 'us-east-1',
                                aws_access_key_id = aws_key_id,
                                aws_secret_access_key = aws_secret_key)
        
        self.firehose_client = firehose_client


    def add_to_stream(self, json_entry):
        client = self.firehose_client


        client.put_record(DeliveryStreamName = 'nasa-datahose-02', 
                            Record={'Data':json_entry}
                        )
        
    
    def check_streams(self):
        client = self.firehose_client
        print(client.describe_delivery_stream(
                DeliveryStreamName='nasa-datahose-02'
            ))

        # print(client.list_delivery_streams())


def main():
    fetch = Data_Fetch()
    hose = Fire_Hose()

    json_entry = fetch.access_api()
    print(json_entry)

    hose.add_to_stream(json_entry)
    # hose.check_streams()

if __name__ == '__main__':
    main()