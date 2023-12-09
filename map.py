def in_for_mAP_true(batch):
  lst=batch[1]
  ground_date=[]
  for i,_ in enumerate(lst):
    t=list(zip(_['labels'],_['boxes']))
    lst_data =[]
    for k in t:
      f=[i,k[0]]
      f.extend(k[1])
      f.insert(2,float(1))
      lst_data.append([int(i) for i in f])
    ground_date.extend(lst_data)
  return ground_datie
