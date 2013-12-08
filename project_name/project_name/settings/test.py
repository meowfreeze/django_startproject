from .base import *

# figure out what the project root should be
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT
TEST_DISCOVER_ROOT = PROJECT_ROOT
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
