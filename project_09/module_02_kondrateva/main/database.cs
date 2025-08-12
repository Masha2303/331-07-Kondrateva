using Npgsql;


namespace database;
public class MyClass
{
    public string connect = "host = localhost; username = postgres; database = postgres; password = KUR03102005kur;";
    public NpgsqlDataReader db(string commandSQL)
    {
        NpgsqlConnection connection = new NpgsqlConnection(connect);
        connection.Open();
        NpgsqlCommand command = new NpgsqlCommand(commandSQL, connection);
        NpgsqlDataReader reader = command.ExecuteReader();
        return reader;
    }
}