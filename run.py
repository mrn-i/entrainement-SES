#!/usr/bin/env python3

from linear_app import app
import os

if __name__ == "__main__":
# Bind to PORT if defined, otherwise default to 5000.

    if os.environ["APP_SETTINGS"] == "config.ProductionConfig" :
        port = int(os.environ.get('PORT', 5000))
        app.run(debug=True, host='0.0.0.0', port=port)
    else :
        app.run(debug=True)

