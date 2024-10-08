#!/usr/bin/env python3
"""
Module that contains asynchronous wait_random function.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    """
    wait_time = random.uniform(0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time
