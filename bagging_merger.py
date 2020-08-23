
filename = 'final_predictions/final_predictions_berttest_subset2epochs_test_set.txt'

predictionssub2=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub2.append(line)

filename = 'final_predictions/final_predictions_berttest_subset4epochs_test_set.txt'

predictionssub4=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub4.append(line)

filename = 'final_predictions/final_predictions_berttest_subset5epochs_test_set.txt'

predictionssub5=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub5.append(line)

filename = 'final_predictions/final_predictions_berttest_subset6epochs_test_set.txt'

predictionssub6=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub6.append(line)

filename = 'final_predictions/final_predictions_berttest_subset7epochs_test_set.txt'

predictionssub7=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub7.append(line)

filename = 'final_predictions/final_predictions_berttest_subset8epochs_test_set.txt'

predictionssub8=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub8.append(line)

filename = 'final_predictions/final_predictions_berttest_subset10epochs_test_set.txt'

predictionssub10=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            predictionssub10.append(line)
            
filename = 'final_predictions_ensembled.txt'

final_predictions_ensembled=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            final_predictions_ensembled.append(line)
            
            
filename = 'final_predictions_best_model_8000_in_subsets.txt'

final_predictions_best_model_8000_in_subsets=[]
with open(filename, 'r') as reader:
    for line in reader:
        line = line.strip()
        if len(line) > 0:
            final_predictions_best_model_8000_in_subsets.append(line)

print(len(predictionssub2))
print(len(predictionssub4))
print(len(predictionssub5))
print(len(predictionssub6))
print(len(predictionssub7))
print(len(predictionssub8))
print(len(predictionssub10))

print(len(final_predictions_best_model_8000_in_subsets))
print(len(final_predictions_ensembled))

matching = 0
not_matching = 0
for i in range(len(final_predictions_ensembled)):
    if final_predictions_ensembled[i] == final_predictions_best_model_8000_in_subsets[i]:
        matching = matching +1
    else:
        not_matching = not_matching +1
        
print(matching)
print(not_matching)
    

import pandas as pd
predictions_df = pd.DataFrame({
    'predictionssub2':predictionssub2,
    'predictionssub4':predictionssub4,
    'predictionssub5':predictionssub5,
    'predictionssub6':predictionssub6,
    'predictionssub7':predictionssub7,
    'predictionssub8':predictionssub8,
    'predictionssub10':predictionssub10,
    
})

print(predictions_df.mode(axis=1))

final_predictions = predictions_df.mode(axis=1).values.tolist()

final_predictions

filename = 'final_predictions/final_predictions.txt'

with open(filename, 'w') as writer:
    for pred in final_predictions:
        writer.write(pred[0])
        writer.write('\n')