#!/bin/bash

echo "Refreshing token"
auth-tokens-refresh

i=0
ERRORS=0
while read -r APP_ID; do
    let i++
    printf "%3d %s: " $i $APP_ID
    JSON=$(mktemp)
    ERROR=$(mktemp)
    apps-list -v "$APP_ID" > "$JSON" 2>"$ERROR"

    #
    # Check if there was an error message (e.g., app was removed)
    #
    if [[ -s "$ERROR" ]]; then
        let ERRORS++
        echo -n "ERROR " && cat $ERROR
        continue
    fi

    #
    # See if it's JSON
    #
    if [[ $(python -m json.tool "$JSON" 2>/dev/null) ]]; then
        EXE_SYS=$(jq '.executionSystem' "$JSON")
        if [[ $EXE_SYS != '"stampede2.tacc.utexas.edu"' ]]; then
            let ERRORS++
            echo "BAD EXECUTION SYSTEM $EXE_SYS"
        else
            echo "OK"
        fi
    else
        let ERRORS++
        echo "BAD JSON"
    fi

    rm "$JSON"
done < "apps"

echo "Done, num errors = $ERRORS"

[[ $ERRORS -gt 0 ]] && exit 1
