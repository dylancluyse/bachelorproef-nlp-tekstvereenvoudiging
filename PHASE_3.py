import csv
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch, os, openai

openai.api_key = "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"
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"

tokenizer_T1 = AutoTokenizer.from_pretrained("philippelaban/keep_it_simple")
model_T1 = AutoModelForCausalLM.from_pretrained("philippelaban/keep_it_simple")

tokenizer_T2 = AutoTokenizer.from_pretrained("haining/scientific_abstract_simplification")
model_T2 = AutoModelForSeq2SeqLM.from_pretrained("haining/scientific_abstract_simplification")

FORMAT = "formaat: vereenvoudigde tekst"

PROMPTS = [
    "Vereenvoudig deze zin",
    "Vereenvoudig deze zin voor scholieren (leeftijd 16-18): vervang moeilijke woorden, behoud gekend jargon, vervang woorden langer dan 18 karakters, schrijf acroniemen voluit, gebruik één synoniem per woordvervanging of geef een korte uitleg, gebruik weinig tot geen cijfergetallen.",
    "Vereenvoudig deze zin door deze op te delen in kortere zinnen van maximaal tien woorden. Verander voornaamwoorden als 'zij', 'hun' of 'hij' in namen. Vervang complexe zinsconstructies en voorzetselzinnen door eenvoudiger alternatieven, maar laat ze ongewijzigd als er geen eenvoudiger optie beschikbaar is."
]

folder_path = 'scripts/pdf/'
original_scientific_papers_csv = [f for f in os.listdir(folder_path)]

for csv_results in original_scientific_papers_csv:                  # Doorloopt alle CSV-bestanden
    if csv_results.endswith('.csv'):                                # CHECK
        with open(folder_path + '/' + csv_results, 'r') as file:    # LEEST CSV BESTAND 
            try:
                for line in file:
                    array = line.split('|')
                    first_column_value = array[0].replace('\n', ' ').strip(' ')   # ORIGINAL
                    second_column_value = array[1].replace('\n', ' ').strip(' ')  # TRANSLATED ORIGINAL
                        
                    if len(first_column_value) > 5:
                        start_id = tokenizer_T1.bos_token_id
                        tokenized_paragraph = [(tokenizer_T1.encode(text=second_column_value) + [start_id])]
                        input_ids = torch.LongTensor(tokenized_paragraph)
                        output_ids = model_T1.generate(input_ids, max_length=200, num_beams=4, do_sample=True, num_return_sequences=8)
                        output_ids = output_ids[:, input_ids.shape[1]:]
                        output = tokenizer_T1.batch_decode(output_ids)
                        output = [o.replace(tokenizer_T1.eos_token, "") for o in output]
                        T1_RESULT = str(output[0]) # T1 simplification

                        INSTRUCTION = "simplify: "
                        encoding = tokenizer_T2(INSTRUCTION + second_column_value, max_length=200, padding='max_length', truncation=True, return_tensors='pt')
                        decoded_ids = model_T2.generate(input_ids=encoding['input_ids'], attention_mask=encoding['attention_mask'], max_length=512, top_p=.9, do_sample=True)
                        result_T2 = tokenizer_T2.decode(decoded_ids[0], skip_special_tokens=True)
                        T2_RESULT = str(result_T2) # T2 simplification


                        results_T3 = []
                        for prompt in PROMPTS:
                            custom_prompt = prompt + f"/// {first_column_value} + /// {FORMAT}"
                            result = openai.Completion.create(
                                prompt=custom_prompt,
                                temperature=0,
                                max_tokens=100,
                                model=COMPLETIONS_MODEL,
                                top_p=0.9,
                                stream=False
                            )["choices"][0]["text"].strip("\n").strip(" ")
                            results_T3.append(f'"{result}"')

                        concat_array = [first_column_value, second_column_value, T1_RESULT, T2_RESULT] + results_T3

                        with open('output_artikel_1.csv', 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(concat_array)

                    else:
                        pass

            except UnicodeDecodeError:
                pass                    