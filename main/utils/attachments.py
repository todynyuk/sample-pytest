import time
from pytest_zebrunner import attach_test_artifact
from pytest_zebrunner import attach_test_screenshot
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
import mss
import logging


def attach_screenshot():
    with mss.mss() as sct:
        filename = sct.shot(mon=-1, output='fullscreen.png')
    attach_test_screenshot('fullscreen.png')


def attach_logs(log_level, message):
    logger = logging.getLogger('logger_name')
    logger.setLevel(log_level)
    logger.addHandler(ZebrunnerHandler())
    logger.info(message)


def attach_recorded_video(self, start_time, end_time, seconds, recorder):
    while True:
        seconds += 1
        time.sleep(1)
        if seconds >= int((end_time - start_time)/2):
            recorder.stop_recording()
            break
    attach_test_artifact("recording.mp4")
