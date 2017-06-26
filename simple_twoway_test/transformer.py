
from kafka import KafkaConsumer, SimpleProducer, KafkaClient
#connect to Kafka server and pass the topic we want to consume
in_topic = 'my-input-topic'
out_topic = 'my-output-topic'
consumer = KafkaConsumer(in_topic, group_id='view', bootstrap_servers=['0.0.0.0:9092'])

#  connect to Kafka for production
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
# Assign a sender topic

#Continuously listen to the connection and print messages as recieved

def transform(in_msg):
	return 'a'+ in_msg


def kafkastream():
	# consume all messages in consumer 
	# (right now this loop never stops)
    for msg in consumer:
        print(msg.value)
        # transform received messages
        out_msg = transform(msg.value)
        # produce transformed measages under a new topic
        producer.send_messages(out_topic,out_msg)

if __name__ == '__main__':
	print("start transforming")
	kafkastream()




