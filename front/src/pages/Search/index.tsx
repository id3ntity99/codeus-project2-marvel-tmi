import { useQuery } from "react-query";
import { useLocation, useParams } from "react-router";
import Avenger from "../../components/Avenger";
import Header from "../../components/header";
import { IavengersInfo } from "../../typings/db";
import { fetcherKeywordAvengers } from "../../utils/api";
import { PostWrapper } from "../Home/styles";

const Search = () => {
  const { search } = useLocation();
  const keyword = new URLSearchParams(search).get("keyword");
  const { isLoading, data: avengersData } = useQuery<IavengersInfo[]>(
    [search, "avengersData"],
    () => fetcherKeywordAvengers(keyword as string)
  );
  return (
    <>
      <>
        <Header />
        {isLoading ? (
          "loading..."
        ) : (
          <PostWrapper>
            {avengersData?.map(avenger => (
              <Avenger key={avenger.id} avengerInfo={avenger} />
            ))}
          </PostWrapper>
        )}
      </>
    </>
  );
};

export default Search;