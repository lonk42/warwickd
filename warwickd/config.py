from pydantic import BaseModel
from typing import List

class Mqtt_broker(BaseModel):
    server: str
    port: int

class Smtp(BaseModel):
    server: str
    port: int

class Mailer(BaseModel):
    from_name: str
    from_address: str
    to_address: str
    subject: str
    smtp: Smtp

class Prometheus(BaseModel):
    enabled: bool
    http_port: int

class Ntp_service(BaseModel):
    topic: str
    enabled: bool = False

class Config(BaseModel):
    mqtt_broker: Mqtt_broker
    mailer: Mailer
    subscriptions: List
    ntp_service: Ntp_service
    prometheus: Prometheus
