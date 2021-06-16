import logging

from .celery import app
from task.models import Task

from parser.account_parser import AccountParser, AccountStoreHelper

logger = logging.getLogger(__name__)


@app.task(bind=True, name="parse_accounts", ignore_result=True)
def parse_accounts(self, username, password):
    try:
        task = Task.objects.filter(celery_task_id=self.request.id)

        account_parser = AccountParser(username, password)
        customer, accounts, statements = account_parser.parse()
        AccountStoreHelper.store(task.get(), customer, accounts, statements)

        task.update(status=Task.Status.DONE)
        logger.info("Task with id '{0}' finished without error.")
    except Exception as e:
        logger.error(
            "An exception has occurred for task {0}: '{1}' {2}".format(
                self.request.id,
                str(e.__class__),
                e
            )
        )
        task.update(status=Task.Status.FAILED)
