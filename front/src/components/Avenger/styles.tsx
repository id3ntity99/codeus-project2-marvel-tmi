import styled from "styled-components";

export const Post = styled.div`
  width: 200px;
  height: 300px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: ${props => props.theme.bgColor.lighter};
`;

export const Name = styled.h3`
  font-weight: 800;
  margin-bottom: 10px;
`;

export const Description = styled.p`
  font-size: 0.9rem;
`;

export const Info = styled.div`
  border-top: 1px solid ${props => props.theme.bgColor.default};
  display: flex;
  justify-content: space-between;
  padding: 10px;
  font-size: 0.7rem;
`;
