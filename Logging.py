import logging

logging.basicConfig(filename= "Logs.log", level = logging.INFO)
logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)
filehandler = logging.FileHandler("logme.txt")
form = logging.Formatter("%(name)s - %(levelname)s : %(asctime)s - %(message)s")
filehandler.setFormatter(form)
logger.addHandler(filehandler)
logging.debug("debugging")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# def f():
	# logger = logging.getLogger("f")
	# logger.setLevel(logging.DEBUG)
	# logger.debug("in der Funktion")
# f()