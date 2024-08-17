import concurrent.futures
from test_crossbrowser import run_google_search_test
# List of browsers
browsers = ["chrome", "firefox", "edge"]

# Execute tests in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_google_search_test, browsers)