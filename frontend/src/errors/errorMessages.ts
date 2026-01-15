export type ApiErrorCode =
  | 'CANNOT_REMOVE_TEAM_LEADER'
  | 'LEADER_NOT_FOUND'
  | 'MEMBER_NOT_FOUND'
  | 'NEW_LEADER_NOT_FOUND'
  | 'TEAM_NOT_FOUND'
  | 'USER_ALREADY_BELONGS_TO_A_TEAM'
  | 'USER_IS_ALREADY_LEADING_ANOTHER_TEAM'
  | 'USER_NOT_FOUND'
  | 'USER_NAME_REQUIRED'; 

  export const errorMessages: Record<ApiErrorCode, string> = {
  CANNOT_REMOVE_TEAM_LEADER: 'O líder da equipe não pode ser removido',
  LEADER_NOT_FOUND: 'Líder não encontrado',
  MEMBER_NOT_FOUND: 'Membro não encontrado',
  NEW_LEADER_NOT_FOUND: 'Líder não encontrado',
  TEAM_NOT_FOUND: 'Equipe não encontrada',
  USER_ALREADY_BELONGS_TO_A_TEAM: 'Usuário já pertence a uma equipe',
  USER_IS_ALREADY_LEADING_ANOTHER_TEAM: 'Usuário já está liderando outra equipe',
  USER_NOT_FOUND: 'Usuário não encontrado',
  USER_NAME_REQUIRED: 'Adicione um nome'
};