from encrypt import haversine

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument("input")
    input = parser.parse_args().input
    print(input)
    print(haversine(52.370216, 4.895168, 52.520008, 13.404954))
