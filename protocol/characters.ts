/** Offline character contract v1. No player model or automatic canon promotion. */
export type Origin = 'originalCharacter' | 'fanfictionCharacter';
export interface Figure { id: string; name: string; origin: Origin }
export interface Trait { id: string; label: string }
export interface FigureInstance {
  id: string; figure_id: string; session_id: string; trait_ids: string[];
}
export interface StoryEvent {
  id: string; session_id: string; position: number;
  roles: { instance_id: string; role_id: string }[];
}
export interface Relationship {
  id: string; session_id: string;
  participants: { instance_id: string; role_id: string }[];
}
export interface StateTransition {
  id: string; instance_id: string; event_id: string; before: string; after: string;
}
export interface Chapter {
  id: string; session_id: string; event_ids: string[];
  promotion?: { decision_path: string };
}
export interface CharacterProtocol {
  version: 1;
  figures: Figure[]; traits: Trait[]; instances: FigureInstance[];
  event_roles: { id: string; label: string }[];
  relationship_roles: { id: string; label: string }[];
  events: StoryEvent[]; relationships: Relationship[];
  transitions: StateTransition[]; chapters: Chapter[];
}
