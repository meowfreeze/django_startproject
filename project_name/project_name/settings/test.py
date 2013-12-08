from .base import *

# figure out what the project root should be
TEST_DISCOVER_TOP_LEVEL = BASE_DIR
TEST_DISCOVER_ROOT = BASE_DIR
TEST_DISCOVER_PATTERN = 'test_*'

DATABASES = {
	"default": {
	"ENGINE": "django.db.backends.sqlite3",
	"NAME": ":memory:",
	"USER": "",
	"PASSWORD": "",
	"HOST": "",
	"PORT": "",
	},
}
