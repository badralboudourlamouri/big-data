from confluent_kafka import Producer
import random
import time

# تهيئة منتج Kafka
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# دالة لإرسال البيانات إلى Kafka
def on_delivery(err, msg):
    if err is not None:
        print(f"فشل في إرسال الرسالة: {err}")
    else:
        print(f"تم تسليم الرسالة إلى {msg.topic()} [{msg.partition()}]")

# محاكاة بيانات من الحساسات
while True:
    status = random.choice(['تشغيل', 'إيقاف', 'خطأ'])
    producer.produce('machine-status', key="machine_id", value=status, callback=on_delivery)
    producer.poll(0)
    time.sleep(2)  # محاكاة إرسال بيانات من الحساس كل 2 ثانية
