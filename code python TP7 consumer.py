from confluent_kafka import Consumer, KafkaError

# تهيئة مستهلك Kafka
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group-مراقبة-الآلات',
    'auto.offset.reset': 'earliest'
})

# الاشتراك في الموضوع
consumer.subscribe(['machine-status'])


# بدء استهلاك الرسائل
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"تم الوصول إلى نهاية القسم في {msg.topic()} [{msg.partition()}] عند الإزاحة {msg.offset()}")
            else:
                print(f"خطأ: {msg.error()}")
        else:
            print(f"تم استقبال الرسالة: {msg.value().decode('utf-8')}")
finally:
    consumer.close()
