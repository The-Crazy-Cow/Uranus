

# check login as root
IS_LOGIN_ROOT(){
    if ["EUID" -ne 0];then
        echo "not login as root : permission denied"
        echo
        return 1
    fi
}

# check package is intall
IS_PACKAGE_INSTALLED(){
    local PACKAGE=$1

    if dpkg -l | grep -q "îi "$PACKAGE" ";then
        return 0
    else
        echo "package : "$PACKAGE" not installed on host"
        echo
        echo "package : "$PACKAGE" is intalling..."
        echo

        if DEBIAN_FRONTEND=nononteractive apt-get install -y "$PACKAGE" > /dev/null 2>&1; then
            echo "package : "$PACKAGE" installed successfully..."
        else
            echo "failed on installing package : "$PACKAGE""
            return 1
        fi
        echo
    fi

    local VERSION=apt-cache policy $PACKAGE | grep -E "(Installed)"
    local CANDIDATE=apt-cache policy $PACKAGE | grep -E "(Candidate)"

    echo "package "$PACKAGE":"$VERSION" -> candidate :"$CANDIDATE""
    echo
    return 0
}