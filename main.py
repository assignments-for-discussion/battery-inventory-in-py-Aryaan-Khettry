def count_batteries_by_usage(cycles):
    # We use a dictionary, "usage_dict", to store the number of batteries of varying charge.
  
  usage_dict = {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  # Iterate through each battery's number of charge-cycles and increment the dictionary values according to the classification given.

  for charge_cycles in cycles:
        if charge_cycles < 0:
            raise Exception("Value cannot be negative")
        if charge_cycles >= 910:
            usage_dict['highCount']+=1
        elif charge_cycles >= 410:
            usage_dict['mediumCount']+=1
        elif charge_cycles >=0:
            usage_dict['lowCount']+=1

  return usage_dict

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting, test case passed! :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
