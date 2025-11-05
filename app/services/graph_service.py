import numpy as np
from sqlalchemy.orm import Session

from app.db.models import SymptomEmbedding


def add_symptom_embedding(db: Session, uid: int, symptom: str, intensity: float, embedding: list[float]):
    embedding_np = np.array(embedding, dtype=np.float32)
    embedding_list = embedding_np.tolist()

    record = SymptomEmbedding(
        user_hmac_id=uid,
        symptom=symptom,
        intensity=intensity,
        embedding=embedding_list
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record
