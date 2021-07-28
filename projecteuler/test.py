import eulerlib, timelog

if __name__ == "__main__":
    timelog.start()
    timelog.end()
    print(timelog.getRuntime())
    print(eulerlib.list_primes())


