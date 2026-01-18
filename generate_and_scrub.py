#!/usr/bin/env python3
"""Generate fake shipping data and scrub patient names with SHA-256."""
from faker import Faker
import pandas as pd
import hashlib
import uuid
import random
from datetime import datetime, timedelta

fake = Faker()

DEVICE_TYPES = [
    "Pacemaker",
    "Insulin Pump",
    "Hearing Aid",
    "CPAP Machine",
    "Orthotic",
    "Prosthetic",
    "Infusion Pump",
]

DELIVERY_STATUSES = ["Delivered", "In Transit", "Delayed", "Failed", "Pending"]


def generate_row():
    shipment_id = str(uuid.uuid4())
    patient_name = fake.name()
    device = random.choice(DEVICE_TYPES)
    lat = round(float(fake.latitude()), 6)
    lon = round(float(fake.longitude()), 6)
    delivery_coords = f"{lat},{lon}"
    status = random.choice(DELIVERY_STATUSES)
    delivery_date = (datetime.now() + timedelta(days=random.randint(-30, 5))).date().isoformat()

    return {
        "ShipmentID": shipment_id,
        "PatientName": patient_name,
        "MedicalDeviceType": device,
        "DeliveryCoordinates": delivery_coords,
        "DeliveryStatus": status,
        "DeliveryDate": delivery_date,
    }


def generate_csv(rows=100, filename="raw_shipping_data.csv"):
    records = [generate_row() for _ in range(rows)]
    df = pd.DataFrame(records)
    df.to_csv(filename, index=False)
    return df


def hash_name(name: str) -> str:
    if not isinstance(name, str):
        name = str(name)
    return hashlib.sha256(name.encode("utf-8")).hexdigest()


def scrub_csv(raw_filename="raw_shipping_data.csv", scrubbed_filename="scrubbed_shipping_data.csv"):
    df = pd.read_csv(raw_filename)
    if "PatientName" not in df.columns:
        raise KeyError("Expected column 'PatientName' in raw CSV")
    df["PatientName"] = df["PatientName"].fillna("").apply(hash_name)
    df.to_csv(scrubbed_filename, index=False)
    return df


def main():
    print("Generating raw CSV (raw_shipping_data.csv)...")
    generate_csv(100, "raw_shipping_data.csv")
    print("Scrubbing PII into scrubbed_shipping_data.csv...")
    scrub_csv("raw_shipping_data.csv", "scrubbed_shipping_data.csv")
    print("Done. Created raw_shipping_data.csv and scrubbed_shipping_data.csv")


if __name__ == "__main__":
    main()
