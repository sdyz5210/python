#!/usr/bin/python
# -*- coding: utf-8 -*-
# python version 2.7.6

#消费者必须先启动

from kafka import KafkaConsumer

# To consume messages
consumer = KafkaConsumer('my-topic',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    # message value is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))