from kafka import KafkaConsumer, SimpleProducer, KafkaClient
import json
from ruleGenLogic import gen_rules

# Consume settings
in_topic = 'test'
consumer = KafkaConsumer(in_topic, group_id='view', bootstrap_servers=['0.0.0.0:9092'])

# Producer settings
out_topic = 'test_reply'
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)


def kafkastream():
    for msg in consumer:
        msg_string = (msg.value).decode("utf-8")

        # SEE OUTPUT LOCALLY FOR TESTING
        print(msg)
        #print(gen_rules(msg_string))
        
        # generate rules and publish to reply stream
        producer.send_messages(out_topic,gen_rules(msg_string))



if __name__ == '__main__':
    print("start transforming")
    kafkastream()