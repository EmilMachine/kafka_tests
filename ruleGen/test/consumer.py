
from kafka import KafkaConsumer
#connect to Kafka server and pass the topic we want to consume
in_topic = 'test_reply'
consumer = KafkaConsumer(in_topic, group_id='view', bootstrap_servers=['0.0.0.0:9092'])
#Continuously listen to the connection and print messages as recieved

def kafkastream():
    for msg in consumer:
        print(msg.value)

if __name__ == '__main__':
	print("start listening")
	kafkastream()