# producer.py

from kafka import SimpleProducer, KafkaClient
import time
#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
# Assign a topic
topic = 'test'

### Gen data
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
iris = load_iris()
data_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                 columns= iris['feature_names'] + ['target'])
# convert all to strings
for col in data_df:
    data_df[col] = data_df[col].astype(str)
data_in = data_df.to_json(orient='records')


def input_emitter():
    # Open the video
    for i in range(1,2):
    # read the image in each frame
        producer.send_messages(topic, data_in)
        # To reduce CPU usage create sleep time of 0.2sec  
        time.sleep(0.2)
    
if __name__ == '__main__':
    print('start emitting...')
    input_emitter()
    print('done emitting...')
