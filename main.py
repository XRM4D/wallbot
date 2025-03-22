import logging
from telegram_publisher import TelegramPublisher

import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting the scheduler...")
    publisher = TelegramPublisher()

    scheduler = AsyncIOScheduler()
    # trigger = CronTrigger(hour='0-22', minute=0)  # Every hour except between 23:00 and 8:00
    trigger = CronTrigger(minute="*")
    scheduler.add_job(publisher.publish, trigger)
    scheduler.start()

    try:
        await asyncio.Event().wait()  # Keep the event loop running
    except (KeyboardInterrupt, SystemExit):
        logger.info("Shutting down the scheduler...")
        scheduler.shutdown()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())