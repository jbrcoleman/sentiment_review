from google.cloud import automl


project_id = "dynamic-aurora-302220"
model_id = "TST8315309572730388480"

def predict(content):
    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

    # Supported mime_types: 'text/plain', 'text/html'
    # https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet
    text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
    payload = automl.ExamplePayload(text_snippet=text_snippet)

    response = prediction_client.predict(name=model_full_id, payload=payload)

    for annotation_payload in response.payload:
        print("Predicted class name: {}".format(annotation_payload.display_name))
        print(
            "Predicted sentiment score: {}".format(
                annotation_payload.text_sentiment.sentiment
            )
        )
        return annotation_payload.text_sentiment.sentiment

if __name__=='__main__':
    predict("test")
