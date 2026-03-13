"""Saturation scheduling for dye processes."""


def saturation_time(volume, flow_rate):
    """Calculate time to saturate a vat at a given flow rate."""
    if flow_rate <= 0:
        raise ValueError("flow rate must be positive")
    return volume / flow_rate


def batch_schedule(vat_volumes, flow_rate):
    """Create a sequential saturation schedule for multiple vats."""
    schedule = []
    cumulative = 0
    for name, volume in vat_volumes:
        duration = saturation_time(volume, flow_rate)
        schedule.append({
            "vat": name,
            "start": cumulative,
            "duration": duration,
            "end": cumulative + duration,
        })
        cumulative += duration
    return schedule


def parallel_capacity(vat_volumes, total_flow):
    """Distribute flow across vats proportionally to their volume."""
    total_volume = sum(v for _, v in vat_volumes)
    if total_volume == 0:
        return []
    return [
        (name, total_flow * vol / total_volume)
        for name, vol in vat_volumes
    ]
