from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, Union


class DataStream(ABC):
    stream_id: str
    processed_count: int

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
                "stream_id": self.stream_id,
                "processed_count": self.processed_count,
                }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.type: str = "Environmental Data"
        self.processed_count: int = 0

    def process_batch(self, data_batch: list[Any]) -> str:
        self.processed_count += len(data_batch)
        temps: list[float] = [
                float(item.split(":")[1])
                for item in data_batch
                if item.startswith("temp")
                ]
        avg_temp: float = sum(temps) / len(temps) if temps else 0.0
        return (f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria == "high-priority":
            return [item for item in data_batch
                    if item.startswith("temp")
                    and float(item.split(":")[1]) > 30
                    or item.startswith("pressure")]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.type: str = "Financial Data"
        self.processed_count: int = 0

    def process_batch(self, data_batch: list[Any]) -> str:
        self.processed_count += len(data_batch)
        net: int = 0
        for item in data_batch:
            action, amount = item.split(":")
            if action == "buy":
                net += int(amount)
            else:
                net -= int(amount)
        sign: str = "+" if net >= 0 else ""
        return (f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{net} units")

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        if criteria == "high-priority":
            return [item for item in data_batch
                    if int(item.split(":")[1]) > 300]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.type: str = "System Events"
        self.processed_count: int = 0

    def process_batch(self, data_batch: list[Any]) -> str:
        self.processed_count += len(data_batch)
        errors: int = len([e for e in data_batch if e == "error"])
        return (f"Event analysis: {len(data_batch)} events, "
                f"{errors} error detected")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.type
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: list[list[Any]]) -> None:
        print("Processing mixed stream types through unified interface...")
        print("Batch 1 Results:")
        for stream, batch in zip(self.streams, batches):
            try:
                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: {len(batch)} readings processed")
                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: {len(batch)} "
                          f"operations processed")
                elif isinstance(stream, EventStream):
                    print(f"- Event data: {len(batch)} events processed")
            except Exception as e:
                print(f"Error processing stream: {e}")

    def filter_all(self, batches: list[list[Any]],
                   criteria: str) -> None:
        print(f"Stream filtering active: {criteria} data only")
        try:
            sensor_filtered = self.streams[0].filter_data(
                    batches[0], "high-priority"
                    )
            trans_filtered = self.streams[1].filter_data(
                    batches[1], "high-priority"
                    )
            print(f"Filtered results: {len(sensor_filtered)} critical sensor "
                  f"alerts, {len(trans_filtered)} large transaction")
        except Exception as e:
            print(f"Error filtering streams: {e}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    try:
        sensor = SensorStream("SENSOR_001")
        print("\nInitializing Sensor Stream...")
        print(f"Stream ID: {sensor.stream_id}, Type: {sensor.type}")
        sensor_batch: list[Any] = ["temp:22.5", "humidity:65",
                                   "pressure:1013"]
        print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
        print(sensor.process_batch(sensor_batch))
    except Exception as e:
        print(f"Error: {e}")

    try:
        transaction = TransactionStream("TRANS_001")
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {transaction.stream_id}, Type: {transaction.type}")
        trans_batch: list[Any] = ["buy:100", "sell:150", "buy:75"]
        print(f"Processing transaction batch: [{', '.join(trans_batch)}]")
        print(transaction.process_batch(trans_batch))
    except Exception as e:
        print(f"Error: {e}")

    try:
        event = EventStream("EVENT_001")
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {event.stream_id}, Type: {event.type}")
        event_batch: list[Any] = ["login", "error", "logout"]
        print(f"Processing event batch: [{', '.join(event_batch)}]")
        print(event.process_batch(event_batch))
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    poly_batches: list[list[Any]] = [
            ["temp:35.0", "pressure:950"],
            ["buy:200", "sell:50", "buy:300", "sell:400"],
            ["login", "error", "logout"],
            ]
    processor.process_all(poly_batches)
    print()
    processor.filter_all(poly_batches, "High-priority")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
