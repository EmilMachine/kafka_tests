
from kafka import KafkaConsumer
import json
from ruleGen import gen_rules
#connect to Kafka server and pass the topic we want to consume
in_topic = 'test'
consumer = KafkaConsumer(in_topic, group_id='view', bootstrap_servers=['0.0.0.0:9092'])
#Continuously listen to the connection and print messages as recieved

def kafkastream():
    for msg in consumer:
        #print(msg)
        msg_string = (msg.value).decode("utf-8")
        print(type(msg_string))
        #msg_string = (msg.value).decode("utf-8")
        print(msg)
        print(gen_rules(msg_string))
        #print(json.loads(msg_string))

if __name__ == '__main__':
    print("start listening")
    kafkastream()