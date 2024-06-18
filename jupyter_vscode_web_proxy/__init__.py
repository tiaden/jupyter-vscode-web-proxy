import os
import shutil
from typing import Any, Callable, Dict, List

"""
  "$VSCODE_WEB" serve-local "$EXTENSION_ARG" --port "${PORT}" --host 127.0.0.1 --accept-server-license-terms --without-connection-token --telemetry-level "${TELEMETRY_LEVEL}" > "${LOG_PATH}" 2>&1 &

"""
def _get_code_server_executable(prog):
    # Find prog in known locations
    other_paths = [
        os.path.join('/opt/vscode-web/bin', prog),
    ]
    if shutil.which(prog):
        return prog

    for op in other_paths:
        if os.path.exists(op):
            return op

    raise FileNotFoundError(f'Could not find {prog} in PATH')



def run_vscode_web() -> Dict[str, Any]:
    def _get_cmd(port):
        extensions_dir = os.getenv("VSCODE_WEB_EXTENSIONS_DIR", "")
        cmd = [
            _get_code_server_executable('code-server'),
            'serve-local' + extensions_dir,
            '--port=' + str(port),
            '--accept-server-license-terms',
            '--host=127.0.0.1',
            '--without-connection-token',
            '--telemetry-level=off'
        ]

        return cmd

    return {
        "command": _get_cmd,
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", vscode.svg
            ),
        },
    }
