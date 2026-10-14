# Lesefragen aus den Begriffsseiten

Diese Fragenentwürfe ergänzen die bestehenden offenen Fragen Q1–Q9. Sie stellen
keine neuen Konfliktbefunde fest und behaupten nicht, dass ihre Antworten fehlen.
Der Antwortstand ist **ungeprüft**. Bestehende Autorentscheidungen gewinnen.

Jeder Term der aktuellen Wiki-Oberfläche erhält **100 zusätzliche Fragen**:
40 Fragen zu fünf redaktionell ausgewählten Themen und 60 Fragen zu fünf
redaktionell ausgewählten Vergleichsterms. Pro Term ist die erste Frage einzeln
formuliert; die weiteren Fragen erkunden die Themen mit gemeinsamen Blickwinkeln.
Die Menge ist ein Arbeitsvorrat, keine Prioritätenliste und kein Maß für offene
Kanonentscheidungen. Ein Vergleich fragt nach einer Verbindung; er setzt sie
nicht als Tatsache voraus.

Die Auswahl der Themen und Vergleichspartner steht in
`Plan/concept/reading-topics.json`. Sie beruht auf der Lektüre der Begriffsseiten,
ihrer unterschiedlichen Quellenlesarten und den bereits sichtbaren offenen
Entscheidungen. Die JSON-Dateien hier sind editierbare Fragebanken; der Builder
weigert sich, bestehende Banken zu überschreiben. Keine Quelldokumente werden
geändert oder an einen externen Modelldienst gesendet.

Jede Bank nennt die Wikiseiten, die bei ihrer Erstellung vorlagen, samt SHA256.
Eine spätere Ergänzung macht die Fragen nicht ungültig: die UI weist dann darauf
hin, die aktuelle Antwortlage erneut zu prüfen. Die Fragen behalten ihre IDs,
z. B. `RQ-aegis-001`, und ihre Adresse `#/questions/reading/RQ-aegis-001`.
Der Ursprungsterm hat genau seinen eigenen Vorrat; die Checkbox in der UI zeigt
zusätzlich Fragen anderer Vorräte, die ihn als Vergleichspartner nennen.

Die UI kann Fragen durchsuchen, eingrenzen und exportieren. Notizen und der
Arbeitsstand **„Lokal beantwortet“** bleiben im Browser; sie ändern weder diese
Dateien noch den Kanon. „Alle Notizen sichern“ exportiert auch Notizen, die der
aktuelle Filter ausblendet. Ein Prüfauftrag verweist auf ID und Repo-Datei und
kopiert keine Quellenpassagen. Agents erhalten denselben Vorrat in
`agents/reading-questions.json` und die einzelnen Adressen im Agent-Index.

```bash
python3 scripts/reading_questions.py check
python3 scripts/reading_questions.py show aegis
python3 scripts/reading_questions.py selftest
```

Zum Beantworten: zuerst den heutigen Kanon und die aktuellen Wikiseiten lesen;
eine vorhandene Antwort, einen Vorschlag, einen echten Quellenkonflikt und eine
unbelegte Annahme getrennt behandeln. Nur eine tatsächlich kapitelrelevante,
ungelöste Frage gehört nach redaktioneller Prüfung in den bestehenden Q-Bereich.
