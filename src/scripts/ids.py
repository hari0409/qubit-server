


scaler = Normalizer().fit(trial)
trial = scaler.transform(trial)

X_trial = np.array(trial)
X_trial

pred=loaded_model.predict(X_trial)

if(pred<0.5):
    pred=0
else:
    pred=1

print(pred)