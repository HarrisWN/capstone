import requests
import pandas as pd


class Base:
    def __init__(self, url="https://covid-193.p.rapidapi.com/history"):
        self.api_url = url
        self.querystring = {"country": "USA"}
        self.headers = {
            "X-RapidAPI-Key": "3c20c601afmsh20169674f0cfbebp191ab2jsna87d6a1626fc",
            "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
        }

        self.get_data()

    def get_data(self):
        response = requests.get(
            self.api_url, headers=self.headers, params=self.querystring
        )
        if response.status_code == 200:
            covid19_dataframe = response.json()["response"][0]
            self.df = pd.DataFrame.from_dict(covid19_dataframe)
        else:
            print("Error: Failed to fetch data")
            self.df = None

    def normalize_json(self):
        if self.df is not None:
            self.df_normal = pd.json_normalize(self.df["tests"])
            return self.df_normal
        else:
            print("No data to normalize")
            return None

    def extract_cases(self):
        if self.df is not None:
            self.df_cases = pd.json_normalize(self.df["cases"])
            self.df_cases_concat = pd.concat(
                [self.df.drop(["cases"], axis=1), self.df_cases], axis=1
            )
            self.casesdf = self.df_cases_concat.rename(
                columns={
                    "new": "new_cases",
                    "active": "active_cases",
                    "critical": "critical_cases",
                    "recovered": "recovered_cases",
                    "1M_pop": "1M_pop_cases",
                    "total": "total_cases",
                }
            )
            return self.casesdf
        else:
            print("No data to extract cases from")
            return None

    def extract_deaths(self):
        if self.df is not None:
            self.df_tests = pd.json_normalize(self.casesdf["tests"])
            self.df_tests_concat = pd.concat(
                [self.casesdf.drop(["tests"], axis=1), self.df_tests], axis=1
            )
            self.covid_total_df = self.df_tests_concat.rename(
                columns={"1M_pop": "1M_pop_tests", "total": "total_tests"}
            )
            return self.covid_total_df
        else:
            print("No data to extract deaths from")
            return None

    def manage_nulls(self):
        if self.covid_total_df is not None:
            self.covid_total_df["new_cases"] = (
                self.covid_total_df["new_cases"].str.replace("+", "").fillna(0)
            )
            self.covid_total_df["new_deaths"] = (
                self.covid_total_df["new_deaths"].str.replace("+", "").fillna(0)
            )

    def manage_datatype(self):
        if self.covid_total_df is not None:
            self.covid_total_df["new_cases"] = pd.to_numeric(
                self.covid_total_df["new_cases"], errors="coerce"
            )
            self.covid_total_df["new_deaths"] = pd.to_numeric(
                self.covid_total_df["new_deaths"], errors="coerce"
            )
            self.covid_total_df["1M_pop_cases"] = pd.to_numeric(
                self.covid_total_df["1M_pop_cases"], errors="coerce"
            )
            self.covid_total_df["1M_pop_deaths"] = pd.to_numeric(
                self.covid_total_df["1M_pop_deaths"], errors="coerce"
            )
            self.covid_total_df["1M_pop_tests"] = pd.to_numeric(
                self.covid_total_df["1M_pop_tests"], errors="coerce"
            )
            self.covid_total_df["time"] = pd.to_datetime(
                self.covid_total_df["time"], format="%Y-%m-%dT%H:%M:%S%z"
            )
            self.covid_total_df["day"] = pd.to_datetime(self.covid_total_df["day"])


if __name__ == "__main__":
    c = Base()
    if c.df is not None:
        print(c.df)
