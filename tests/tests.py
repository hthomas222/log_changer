from test_script import ip_viewer, pid_viewer, ip_replacer, pid_replacer


def set_up():
    with open("test_file.log") as testy:
        t = testy.readlines()

    with open("test.log", "w") as test:
        for i in t:
            test.writelines(i)

def test_ipviewer():
    ips = ip_viewer()
    assert isinstance(ips, list)

def test_pidviewer():
    pids = pid_viewer()
    assert isinstance(pids, list)

def test_ip_replacer():
    with open("test.log", "a") as r:
        r.writelines("2026-10-02 08:12:05 INFO  [auth] pid=1842  Successful login   user=admin     ip=192.168.1.1  method=password\n")
    ip_replacer("192.168.1.1", "10.0.0.100")
    with open("test.log") as s:
        content = s.read()
    assert "192.168.1.1" not in content
    assert "10.0.0.100" in content

def test_pid_replacer():
    with open("test.log", "a") as r:
        r.writelines("2026-10-02 08:12:05 INFO  [auth] pid=1842  Successful login   user=admin     ip=192.168.1.1  method=password\n")
    pid_replacer("1842", "1843")
    with open("test.log") as s:
        content = s.read()
    assert "1842" not in content
    assert "1843" in content


set_up()
test_ipviewer()
test_pidviewer()
test_ip_replacer()
test_pid_replacer()

