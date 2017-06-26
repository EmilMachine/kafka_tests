# producer.py

from kafka import SimpleProducer, KafkaClient
import time
#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
# Assign a topic
topic = 'my-input-topic'

def input_emitter():
    # Open the video
    for i in range(1,100):
    # read the image in each frame
        producer.send_messages(topic, str(i))
        # To reduce CPU usage create sleep time of 0.2sec  
        time.sleep(0.2)
    
if __name__ == '__main__':
    print('start emitting...')
    input_emitter()
    print('done emitting...')
