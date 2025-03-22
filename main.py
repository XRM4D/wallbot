from telegram_publisher import TelegramPublisher

import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

async def main():
    publisher = TelegramPublisher()

    scheduler = AsyncIOScheduler()
    # trigger = CronTrigger(hour='0-22', minute=0)  # Every hour except between 23:00 and 8:00
    trigger = CronTrigger(minute="*")
    scheduler.add_job(publisher.publish, trigger)
    scheduler.start()

    try:
        await asyncio.Event().wait()  # Keep the event loop running
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == "__main__":
    asyncio.run(main())