import numpy as np
import random
import time

np.random.seed(int(time.time()))
random.seed(int(time.time()))


if __name__ == '__main__':
  N_SAMPLES = 1000000
  RATE_DISCOUNT = 0.7
  RATE_ABORTION = 0.2

  count_boy = 0
  count_girl = 0

  for i_sample in range(N_SAMPLES):
    pregnant_count = 0
    get_pregnant = True
    children = []
    while get_pregnant:
      sex = random.choice(['boy', 'girl'])

      if sex == 'boy':
        count_boy += 1
        children.append(sex)
      elif (np.random.sample() >= RATE_ABORTION):
        count_girl += 1
        children.append(sex)

      pregnant_count += 1

      if sex == 'boy':
        get_pregnant = False
      else:
        get_pregnant = (np.random.sample() < RATE_DISCOUNT**(pregnant_count-1))

    #print(children)

    if i_sample % 1000 == 0:
      print('progress: {}/{}'.format(i_sample, N_SAMPLES))

  total = count_boy + count_girl
  rate_boy = float(count_boy) / float(total)
  rate_girl = float(count_girl) / float(total)
  print('total: {}, boy: {} ({}), girl: {} ({})'.format(
    total,
    count_boy, np.round(rate_boy * 100, 2),
    count_girl, np.round(rate_girl * 100, 2),
  ))


